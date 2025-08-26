class player:
    def __init__(self,jn,name,runs,wickets,team):
        self.jn=jn
        self.name=name
        self.runs=runs
        self.wickets=wickets
        self.team=team

# set methods
    def setjn(self,jn):
        self.jn=jn

    def setname(self,name):
        self.name=name

    def setruns(self,runs):
        self.runs=runs

    def setwickets(self,wickets):
        self.wickets=wickets

    def setteam(self,team):
        self.team=team

# get methods
    def getjn(self):
        return self.jn
    
    def getname(self):
        return self.name
    
    def getruns(self):
        return self.runs
    
    def getwickets(self):
        return self.wickets
    
    def getteam(self):
        return self.team
    
    def display(self):
        print(f"jersey no: {self.jn}, name: {self.name}, runs: {self.runs}, wickets: {self.wickets}, team: {self.team}")

# ------TEAM RCB------#

RCB=[

    player(18,"Virat Kohli",1500,15,"RCB"),
    player(7, "Faf du Plessis", 1200, 2, "RCB"),
    player(32, "Glenn Maxwell", 900, 15, "RCB"),
    player(99, "Mohammed Siraj", 200, 25, "RCB"),
    player(36, "Harshal Patel", 300, 28, "RCB")
]

# ------TEAM PBK------#
PBK=[

    player(17,"Shikhar Dhawan",1100,5,"PBK"),
    player(5, "Liam Livingstone", 850, 10, "PBK"),
    player(10, "Arshdeep Singh", 150, 22, "PBK"),
    player(23, "Kagiso Rabada", 100, 26, "PBK"),
    player(77, "Sam Curran", 600, 18, "PBK")
]

# ------TEAM MI------#
MI=[

    player(45, "Rohit Sharma", 1300, 2, "MI"),
    player(33, "Ishan Kishan", 950, 1, "MI"),
    player(17, "Suryakumar Yadav", 1400, 0, "MI"),
    player(99, "Jasprit Bumrah", 120, 30, "MI"),
    player(93, "Hardik Pandya", 800, 20, "MI")
]

# ------TEAM GT------#
GT=[

    player(7, "Shubman Gill", 1400, 2, "GT"),
    player(1, "David Miller", 1000, 1, "GT"),
    player(33, "Rahul Tewatia", 600, 12, "GT"),
    player(99, "Rashid Khan", 300, 35, "GT"),
    player(9, "Mohammed Shami", 100, 28, "GT")
]

# ------TEAM CSK------#
CSK=[

    player(7, "MS Dhoni", 1200, 1, "CSK"),
    player(9, "Ruturaj Gaikwad", 1100, 0, "CSK"),
    player(18, "Ambati Rayudu", 900, 2, "CSK"),
    player(3, "Deepak Chahar", 150, 25, "CSK"),
    player(55, "Dwayne Bravo", 700, 30, "CSK")
]

# IPL2025 DATABASE

IPL2025_DB={

    "RCB": RCB,
    "PBK": PBK,
    "MI": MI,
    "GT": GT,
    "CSK": CSK
}

# Display all players of a team based on user input

team_name = input("Enter team name (RCB/MI/GT/PBK): ").upper()
if team_name in IPL2025_DB:
    print(f"\nPlayers of {team_name}: ")
    for player in IPL2025_DB[team_name]:
        player.display()
else:
    print("Team not found in IPL 2025 database.")
    

# TASK 1
team_name=(input("Enter team name to find batsman who scored > 1000 runs: ").upper())
if team_name in IPL2025_DB:
    print(f"\nBatsman from {team_name} who scored >1000 runs")
    for player in IPL2025_DB[team_name]:
        if player.getruns()>1000:
            player.display()
else:
    print("Team not found in IPL 2025 database.")

# TASK 2
team_name=(input("Enter team name to find bowlers who took > 20 wickets: ").upper())
if team_name in IPL2025_DB:
    print(f"\nBowlers from {team_name} who took >20 wickets")
    for player in IPL2025_DB[team_name]:
        if player.getwickets() >20 :
            player.display()
else:
    print("Team not found in IPL 2025 database.")

# TASK 3
team_name=(input("Enter team name to find players whose name contains 'r': ").upper())
if team_name in IPL2025_DB:
    print(f"\nPlayers from {team_name} whose name contains 'r':")
    for player in IPL2025_DB[team_name]:
        if "r" in player.getname().lower():
            player.display()
else:
    print("Team not found in IPL 2025 database.")


