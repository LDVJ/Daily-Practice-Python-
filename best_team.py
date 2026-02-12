def find_winner(india_points, australia_points, india_matches, australia_matches):
    if india_points != australia_points:
        print("India" if india_points > australia_points else "Australia")
    elif india_matches != australia_matches:
        print("India" if india_matches < australia_matches else "australia")
    else:
        print("Play another game!")


i_points = int(input("Enter India points: "))
a_points = int(input("Enter Australia points: "))
i_matches = int(input("Enter Indian matches: "))
a_matches = int(input("Enter Australia matches: "))

find_winner(india_points=i_points,australia_points=a_points,india_matches=i_matches,australia_matches=a_matches)
