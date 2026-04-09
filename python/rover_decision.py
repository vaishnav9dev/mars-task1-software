# Problem: Simulate rover decision-making system
# Approach: Combine multiple conditions similar to a behavior tree

def rover_decision(battery, obstacle, signal):

    # Priority 1: Safety
    if battery < 20:
        return "Return to Base"

    # Priority 2: Obstacle avoidance
    if obstacle:
        return "Avoid Obstacle"

    # Priority 3: Communication stability
    if signal == "weak":
        return "Stabilize Communication"

    # Default action
    return "Continue Mission"


if __name__ == "__main__":
    battery = int(input("Battery (%): "))
    obstacle = input("Obstacle detected (yes/no): ").lower() == "yes"
    signal = input("Signal strength (strong/weak): ")

    decision = rover_decision(battery, obstacle, signal)

    print("Rover Decision:", decision)


# Next Step:
# This logic can be extended into a full behavior tree system
