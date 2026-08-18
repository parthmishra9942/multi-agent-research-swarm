from research_swarm.planner import LeadPlannerAgent, WebScoutWorker, DataAnalystWorker
from research_swarm.critic import AdversarialCriticAgent
from research_swarm.synthesizer import ExecutiveReportSynthesizer

def test_full_swarm_orchestration():
    planner = LeadPlannerAgent()
    state = planner.plan("State of Enterprise Autonomous Agents in 2026")
    assert len(state.tasks) == 3

    # Workers execute
    scout = WebScoutWorker()
    analyst = DataAnalystWorker()
    for task in state.tasks:
        if task.assigned_worker == "web_scout":
            scout.execute(task)
        else:
            analyst.execute(task)
        assert task.status == "COMPLETED"

    # Critic audit
    critic = AdversarialCriticAgent()
    state = critic.review(state)
    assert len(state.critic_feedback) > 0

    # Synthesizer
    synth = ExecutiveReportSynthesizer()
    report = synth.synthesize(state)
    assert "# Executive Intelligence Brief" in report
    assert "Gartner AI Forecast" in report
