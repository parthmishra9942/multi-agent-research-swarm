import time
from research_swarm.planner import LeadPlannerAgent, WebScoutWorker, DataAnalystWorker
from research_swarm.critic import AdversarialCriticAgent
from research_swarm.synthesizer import ExecutiveReportSynthesizer

print("=== Multi-Agent Research Swarm End-to-End Orchestration Benchmark ===")
planner = LeadPlannerAgent()
scout = WebScoutWorker()
analyst = DataAnalystWorker()
critic = AdversarialCriticAgent()
synth = ExecutiveReportSynthesizer()

t0 = time.perf_counter()
state = planner.plan("Scaling Compute Limits in LLM Post-Training")
for task in state.tasks:
    if task.assigned_worker == "web_scout":
        scout.execute(task)
    else:
        analyst.execute(task)
state = critic.review(state)
report = synth.synthesize(state)
t1 = time.perf_counter()

print(f"Sub-Tasks Dispatched & Resolved: {len(state.tasks)}")
print(f"Total Synthesis Latency: {(t1 - t0)*1000:.2f} ms")
print(f"Generated Dossier Length: {len(report)} characters")
print(f"Critic Audit Passed: {'Consistency audit passed' in state.critic_feedback[0]}")
