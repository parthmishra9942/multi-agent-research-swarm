from research_swarm.state import SwarmState

class ExecutiveReportSynthesizer:
    """Fuses multi-agent findings into a structured, executive-ready Markdown dossier."""
    def synthesize(self, state: SwarmState) -> str:
        report = []
        report.append(f"# Executive Intelligence Brief: {state.objective}")
        report.append("> Generated autonomously by Hierarchical Multi-Agent Research Swarm\n")
        report.append("## 📋 Executive Summary")
        report.append(f"This intelligence dossier examines **{state.objective}** through parallel multi-agent inquiry across market dynamics, technical scaling bottlenecks, and competitor positioning.\n")

        report.append("## 🔬 Core Findings by Domain")
        all_citations = []
        for task in state.tasks:
            report.append(f"### {task.topic}")
            for finding in task.raw_findings:
                report.append(f"- {finding}")
            all_citations.extend(task.citations)
            report.append("")

        report.append("## 🛡️ Adversarial Audit & Quality Assurance")
        for fb in state.critic_feedback:
            report.append(f"- **Audit Status:** {fb}")
        report.append("")

        report.append("## 📚 Primary Source Citations")
        for idx, cite in enumerate(set(all_citations), 1):
            report.append(f"[{idx}] {cite}")

        final_text = "\n".join(report)
        state.final_report = final_text
        return final_text
