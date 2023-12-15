"""Calculate RequiredRunRate : A team is chasing the
target set in a one-day international match. The
objective is to compute the required run rate. The
following have been provided as input: target,
maxOvers, currentScore, oversBowled."""

def calculate_required_run_rate(target, max_overs, current_score, overs_bowled):
    overs_remaining = max_overs - overs_bowled
    required_run_rate = (target - current_score) / overs_remaining if overs_remaining > 0 else "Invalid input"
    return required_run_rate

target_input = int(input("Enter the target: "))
max_overs_input = int(input("Enter the maximum overs: "))
current_score_input = int(input("Enter the current score: "))
overs_bowled_input = int(input("Enter the overs bowled: "))

result = calculate_required_run_rate(target_input, max_overs_input, current_score_input, overs_bowled_input)

print(result)
