user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Spy:
    def __init__(self,user2_id="codetree", user2_level=10):
        self.u2id = user2_id
        self.u2level = user2_level
spy = Spy()
print(f"user {spy.u2id} lv {spy.u2level}")
spy = Spy(user2_id,user2_level)
print(f"user {spy.u2id} lv {spy.u2level}")
