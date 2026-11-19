# frozen_string_literal: true

require "open3"

module Jekyll
  class GitHistoryGenerator < Generator
    safe true
    priority :highest

    FIELD_SEPARATOR = "\x1f"

    def generate(site)
      ensure_full_history(site.source)

      site.pages.each do |page|
        next unless page.path&.end_with?(".md")

        history = history_for(site.source, page.path)
        page.data["git_history"] = history if history
      end
    end

    private

    def ensure_full_history(root)
      output, = Open3.capture2("git", "-C", root, "rev-parse", "--is-shallow-repository")
      return unless output.strip == "true"

      _, error, status = Open3.capture3(
        "git", "-C", root, "fetch", "--unshallow", "--quiet", "origin"
      )
      return if status.success?

      Jekyll.logger.warn("Git history:", "전체 기록을 가져오지 못했습니다: #{error.strip}")
    rescue StandardError => error
      Jekyll.logger.warn("Git history:", error.message)
    end

    def history_for(root, path)
      format = "%aN%x1f%aE%x1f%aI"
      output, error, status = Open3.capture3(
        "git", "-C", root, "log", "--follow", "--format=#{format}", "--", path
      )
      unless status.success?
        Jekyll.logger.warn("Git history:", "#{path}: #{error.strip}")
        return nil
      end

      commits = output.lines.filter_map do |line|
        name, email, authored_at = line.strip.split(FIELD_SEPARATOR, 3)
        next unless name && email && authored_at

        { "name" => name.strip, "email" => email.strip.downcase, "date" => authored_at.strip }
      end
      return nil if commits.empty?

      current_name = {}
      commits.each { |commit| current_name[commit["email"]] ||= commit["name"] }

      contributors = []
      seen = {}
      commits.reverse_each do |commit|
        email = commit["email"]
        next if seen[email]

        contributors << current_name[email]
        seen[email] = true
      end

      newest = commits.first
      oldest = commits.last
      {
        "author" => current_name[oldest["email"]],
        "last_editor" => current_name[newest["email"]],
        "last_modified" => newest["date"][0, 10],
        "contributors" => contributors
      }
    end
  end
end
