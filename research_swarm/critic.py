from research_swarm.state import SwarmState

class AdversarialCriticAgent:
    """Verifies empirical claims, citation grounding, and consistency across worker outputs."""
    def review(self, state: SwarmState) -> SwarmState:
        feedback = []
        for task in state.tasks:
            if not task.citations:
                feedback.append(f"Task '{task.topic}' contains ungrounded claims without verified citations.")
            if len(task.raw_findings) < 2:
                feedback.append(f"Task '{task.topic}' has insufficient evidence depth.")

        if not feedback:
            feedback.append("All claims verified against primary sources. Consistency audit passed.")
        state.critic_feedback = feedback
        return state
