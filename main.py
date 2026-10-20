print("School Member Club Badge")

member_name=input("Member Name: ")
club_name=input("Club Name: ")

member_number=8
points=9.5
is_active=True
print(f"Member Number: {member_number} -> {type(member_number)}")
print(f"Points: {points} -> {type(points)}")
print(f"Active: {is_active} -> {type(is_active)}")

badge_code=member_name[0:3] + club_name[-1] + str(member_number)
print(f"Badge Code: {badge_code}\n")

print("===== Club Badge =====")
print(f"Member: {member_name}")
print(f"Club: {club_name}")
print(f"Code: {badge_code}")
print(f"Points: {points} | Active: {is_active}")