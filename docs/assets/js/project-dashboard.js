(() => {
  const root = document.getElementById("project-dashboard");
  if (!root) return;

  const dataUrl = new URL("../../assets/data/project-dashboard.json", window.location.href);
  const cleanStatus = (value = "") => value.replace(/^[🟢🟡🔵🟠🔴⚪🟣]\s*/u, "").trim().toUpperCase();
  const escapeHtml = (value = "") => String(value).replace(/[&<>'"]/g, (char) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;"
  })[char]);
  const statusOrder = ["DURING", "WRITING", "WAITING", "TODO", "DONE", "PUBLISHED", "REVISION"];
  const statusLabel = {
    DURING: "🟢 진행 중", WRITING: "🟢 작성 중", WAITING: "🟡 대기",
    TODO: "⚪ 예정", DONE: "🔵 완료", PUBLISHED: "🔵 출판", REVISION: "🟠 리비전"
  };
  const label = (value) => statusLabel[cleanStatus(value)] || value || "미정";

  const boot = async () => {
    try {
      const response = await fetch(`${dataUrl}?v=${Date.now()}`, { cache: "no-store" });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();
      render(data);
    } catch (error) {
      root.innerHTML = `<p class="project-dashboard__error">프로젝트 데이터를 불러오지 못했습니다. 잠시 후 다시 확인해 주세요.</p>`;
      console.error("Project dashboard:", error);
    }
  };

  const render = (data) => {
    const projects = data.projects || [];
    const tasks = data.tasks || [];
    const people = [...new Set(projects.flatMap((p) => [p.lead, ...(p.member || "").split("/")]).map((x) => x.trim()).filter(Boolean))].sort((a, b) => a.localeCompare(b, "ko"));
    const projectStatuses = [...new Set(projects.map((p) => cleanStatus(p.status)).filter(Boolean))]
      .sort((a, b) => statusOrder.indexOf(a) - statusOrder.indexOf(b));

    root.innerHTML = `
      <div class="pd-meta"><span>최종 갱신 ${escapeHtml(data.updatedAt || "-")}</span><span>공개용 Project·Task 데이터</span></div>
      <div class="pd-stats">
        <div class="pd-stat"><span class="pd-stat__value">${projects.length}</span><span class="pd-stat__label">전체 프로젝트</span></div>
        <div class="pd-stat"><span class="pd-stat__value">${projects.filter((p) => ["DURING", "WRITING"].includes(cleanStatus(p.status))).length}</span><span class="pd-stat__label">진행·작성 중</span></div>
        <div class="pd-stat"><span class="pd-stat__value">${tasks.length}</span><span class="pd-stat__label">등록 업무</span></div>
        <div class="pd-stat"><span class="pd-stat__value">${tasks.filter((t) => cleanStatus(t.status) === "WAITING").length}</span><span class="pd-stat__label">대기 업무</span></div>
      </div>
      <div class="pd-controls">
        <input id="pd-search" type="search" placeholder="프로젝트·업무 검색" aria-label="프로젝트 및 업무 검색">
        <select id="pd-status" aria-label="상태 필터"><option value="">모든 상태</option>${projectStatuses.map((s) => `<option value="${escapeHtml(s)}">${escapeHtml(label(s))}</option>`).join("")}</select>
        <select id="pd-person" aria-label="담당자 필터"><option value="">모든 담당자</option>${people.map((p) => `<option value="${escapeHtml(p)}">${escapeHtml(p)}</option>`).join("")}</select>
      </div>
      <div id="pd-results"></div>`;

    const search = root.querySelector("#pd-search");
    const status = root.querySelector("#pd-status");
    const person = root.querySelector("#pd-person");
    const results = root.querySelector("#pd-results");

    const update = () => {
      const query = search.value.trim().toLowerCase();
      const selectedStatus = status.value;
      const selectedPerson = person.value;
      const matches = projects.filter((project) => {
        const projectTasks = tasks.filter((task) => task.projectId === project.id);
        const searchable = [project.id, project.name, project.cohort, project.lead, project.member, ...projectTasks.map((task) => task.name)].join(" ").toLowerCase();
        return (!query || searchable.includes(query))
          && (!selectedStatus || cleanStatus(project.status) === selectedStatus)
          && (!selectedPerson || `${project.lead}/${project.member}`.split("/").map((x) => x.trim()).includes(selectedPerson));
      });
      const visibleIds = new Set(matches.map((p) => p.id));
      const visibleTasks = tasks.filter((task) => visibleIds.has(task.projectId) && (!query || [task.id, task.name, task.assignee].join(" ").toLowerCase().includes(query) || matches.some((p) => p.id === task.projectId && [p.id, p.name].join(" ").toLowerCase().includes(query))));

      const statusCounts = statusOrder.map((key) => ({ key, count: visibleTasks.filter((t) => cleanStatus(t.status) === key).length })).filter((item) => item.count);
      results.innerHTML = `
        <h2 class="pd-section-title">프로젝트</h2>
        <div class="pd-status-summary">${statusCounts.map((s) => `<span class="pd-chip">${escapeHtml(label(s.key))} ${s.count}</span>`).join("")}</div>
        <div class="pd-table-wrap"><table class="pd-table">
          <thead><tr><th>ID</th><th>프로젝트</th><th>연구 대상</th><th>책임자</th><th>담당자</th><th>상태</th><th>업무</th></tr></thead>
          <tbody>${matches.length ? matches.map((p) => `<tr>
            <td class="pd-id">${escapeHtml(p.id)}</td><td><span class="pd-project-name">${escapeHtml(p.name)}</span></td>
            <td>${escapeHtml(p.cohort || "-")}</td><td>${escapeHtml(p.lead || "-")}</td><td>${escapeHtml(p.member || "-")}</td>
            <td><span class="pd-chip">${escapeHtml(label(p.status))}</span></td>
            <td><span class="pd-task-count">${tasks.filter((t) => t.projectId === p.id).length}</span></td>
          </tr>`).join("") : `<tr><td colspan="7" class="pd-empty">조건에 맞는 프로젝트가 없습니다.</td></tr>`}</tbody>
        </table></div>
        <h2 class="pd-section-title">업무</h2>
        <div class="pd-task-list">${visibleTasks.length ? visibleTasks.map((task) => {
          const project = projects.find((p) => p.id === task.projectId);
          return `<article class="pd-task"><div><div class="pd-task__title">${escapeHtml(task.name)}</div><div class="pd-task__meta">${escapeHtml(task.id)} · ${escapeHtml(project?.name || task.projectId)}</div></div><span class="pd-chip">${escapeHtml(label(task.status))}</span><span class="pd-muted">${escapeHtml(task.assignee || "담당자 미정")}${task.dueDate ? ` · ${escapeHtml(task.dueDate)}` : ""}</span></article>`;
        }).join("") : `<p class="pd-empty">조건에 맞는 업무가 없습니다.</p>`}</div>`;
    };

    [search, status, person].forEach((control) => control.addEventListener("input", update));
    update();
  };

  boot();
})();
