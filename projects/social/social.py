import random
from collections import deque

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User: ({repr(self.name)})"

class SocialGraph:
    def __init__(self):
        # self.last_id = 0
        # self.users = {}
        # self.friendships = {}
        self.reset()

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        # self.last_id = 0
        # self.users = {}
        # self.friendships = {}
        self.reset()
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        possible_friendships = []
        
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendships = possible_friendships[i]
            self.add_friendship(friendships[0], friendships[1])

    def bfs(self, start, end):
        q = deque()
        q.append([start])

        visited = set()

        while len(q) > 0:
            path = q.popleft()
            v = path[-1]
            if v not in visited:
                if v == end:
                    return path
                visited.add(v)
                for neighbor in list(self.friendships[v]):
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.append(new_path)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # add itself
        visited[user_id] = [user_id]
        # add all direct friend
        for f in list(self.friendships[user_id]):
            visited[f] = [user_id, f]
        # bfs on unvisited user
        for u in list(self.users):
            # if unvisited
            if u not in visited:
                # bfs(start, end, friends)
                path = self.bfs(user_id, u)
                # if path is valid
                if path:
                    # add path
                    visited[u] = path

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
