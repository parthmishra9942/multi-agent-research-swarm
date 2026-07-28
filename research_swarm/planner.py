from typing import List
from research_swarm.state import SwarmState, ResearchTask

class LeadPlannerAgent:
    """Decomposes high-level research brief into parallel worker subtasks."""
    def plan(self, objective: str) -> SwarmState:
        tasks = [
            ResearchTask(
                task_id="task_market",
                topic="Market & Economic Drivers",
                instructions="Analyze market capitalization, TAM, and growth forecasts.",
                assigned_worker="web_scout"
            ),
            ResearchTask(
                task_id="task_tech",
                topic="Technical Architecture & Bottlenecks",
                instructions="Identify core algorithmic trade-offs, compute constraints, and scaling limits.",
                assigned_worker="data_analyst"
            ),
            ResearchTask(
                task_id="task_competitors",
                topic="Competitive Landscape",
                instructions="Map key players, open-source alternatives, and defensibility.",
                assigned_worker="web_scout"
            )
        ]
        return SwarmState(objective=objective, tasks=tasks)

class WebScoutWorker:
    def execute(self, task: ResearchTask) -> ResearchTask:
        if "market" in task.topic.lower():
            task.raw_findings = [
                "Global AI agent market projected to surpass $47.1B by 2030 (CAGR 44.8%).",
                "Enterprise software spending pivoting from static SaaS seats to outcome-based agent billing."
            ]
            task.citations = ["Gartner AI Forecast 2026", "Morgan Stanley Cloud Report"]
        else:
            task.raw_findings = [
                "Open-weights alternatives (Llama 3, Mistral) closing gap with proprietary frontier models.",
                "Primary moat shifting toward proprietary evaluation data and private tooling integrations."
            ]
            task.citations = ["HuggingFace Leaderboard", "SemiAnalysis Infrastructure Brief"]
        task.status = "COMPLETED"
        return task

class DataAnalystWorker:
    def execute(self, task: ResearchTask) -> ResearchTask:
        task.raw_findings = [
            "Inference cost scales linearly with context length; KV-cache paged attention reduces memory fragmentation by 53%.",
            "Multi-agent reasoning loops achieve 28% higher task accuracy on SWE-bench compared to single-pass prompting."
        ]
        task.citations = ["Berkeley vLLM Paper", "SWE-bench 2026 Meta-Analysis"]
        task.status = "COMPLETED"
        return task
