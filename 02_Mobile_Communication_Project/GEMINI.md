# Project Instructions & Agent Guidelines: Mobile Communications: Wireless Audio Link

> [!info] Project Context
> - **Project ID**: `PRJ-MCOM`  
> - **Course**: `61ECE314 — Mobile Communications (WS 2026/2027)`  
> - **Assigned Team**: Thuy Tien, Nguyen Huynh Van Phuong, Quang Thien (3 Members)  
> - **Category**: 3-Person Trio  
> - **Shared Plan & Specs**: [`PROJECT_PLAN_MOBILE_COMM.md`](PROJECT_PLAN_MOBILE_COMM.md) & [`WIRELESS_IEM_TRANSCEIVER_MASTER_PLAN.md`](WIRELESS_IEM_TRANSCEIVER_MASTER_PLAN.md)  
> - **Shared Progress Tracker**: [`MCOM_Project_Progress_Tracker.xlsx`](MCOM_Project_Progress_Tracker.xlsx)  
> - **Master Sync Script**: `python "G:\My Drive\Study\VGU\VGU Sem5\sync_sem5_dashboard.py" --mode auto`  

---

## 1. Operational Directives for AI Agent

When a new session or chat is opened in this shared workspace folder, the Agent MUST adhere to the following rules:

### 1.1 Context & Technical Scope Awareness
- Dedicated shared workspace for **PRJ-MCOM (Mobile Communications: Real-Time Wireless Audio Link in GNU Radio)**.
- Holds the team's shared progress tracker [`MCOM_Project_Progress_Tracker.xlsx`](MCOM_Project_Progress_Tracker.xlsx) and technical plans [`PROJECT_PLAN_MOBILE_COMM.md`](PROJECT_PLAN_MOBILE_COMM.md) / [`WIRELESS_IEM_TRANSCEIVER_MASTER_PLAN.md`](WIRELESS_IEM_TRANSCEIVER_MASTER_PLAN.md).
- Keep all documentation, UI text, messages, and code comments in **English** by default.

### 1.2 Holistic Plan & Progress Maintenance
When tasks or technical specifications are refined:
1. Update [`PROJECT_PLAN_MOBILE_COMM.md`](PROJECT_PLAN_MOBILE_COMM.md) or [`MCOM_Project_Progress_Tracker.xlsx`](MCOM_Project_Progress_Tracker.xlsx).
2. Ensure flowgraph versions, modulation schemes, and gate milestones match across files.

### 1.3 Cognitive Context-Aware Synchronization
When the user requests synchronization (e.g., *"Sync"*, *"đồng bộ"*, *"cập nhật dashboard"*, or `/vgu-sem5-sync`):
- **DO NOT BLINDLY OVERWRITE FILES**:
  1. **Read & Diff First**: Run diff inspection via `python "G:\My Drive\Study\VGU\VGU Sem5\sync_sem5_dashboard.py" --mode diff --project PRJ-MCOM`.
  2. **Analyze Semantic Changes**: Understand teammate or local changes in GNU Radio flowgraphs or work packages.
  3. **Decide & Execute Targeted Tool**: Run the targeted synchronization autonomously in the background via `run_command` (e.g., `python "G:\My Drive\Study\VGU\VGU Sem5\sync_sem5_dashboard.py" --project PRJ-MCOM --mode auto`). **NEVER** instruct the user to type terminal commands manually.
  4. **Cognitive Handover Report**: Present a clear summary of semantic differences detected and tools executed in Vietnamese.

---

## 2. Documentation and Obsidian Formatting Rules

- **Zero Icons and Emojis**: Strictly DO NOT use emojis or decorative icons in headings, lists, tables, or document bodies.
- **Obsidian-Compatible Headings & Syntax**: Use standard markdown headings (`#`, `##`, `###`), standard tables, and clean bulleted lists.
- **Obsidian Callouts**: Use clean Obsidian callouts (`> [!info]`, `> [!note]`, `> [!warning]`, `> [!important]`) without icons.
- **Mathematical Formulations**: Always format math with LaTeX `$ ... $` and `$$ ... $$`.

---

## 3. Privacy & Data Confidentiality
- **ZERO personal examination data**: Never add re-exam schedules, personal availability, or test preparation notes into team-shared files.
