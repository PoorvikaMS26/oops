class InstagramAccount:
    def __init__(self, account_name, password):
        self.account_name = account_name
        self._private_reels = []
        self.__archived_reels = []
        self.__password = password
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print("Private reel added successfully")
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print("Archived reel added successfully")
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only followers can view private reels")
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully")
        else:
            print("Incorrect old password")

acc = InstagramAccount("poorvika_account", "1234")
acc.add_private_reel("Travel vlog")
acc.display_private_reels(True)
acc.add_archived_reel("Old Reel 1")
acc.display_archived_reels("1234")
print(acc.get_archived_reels("1234"))
acc.set_password("1234", "5678")