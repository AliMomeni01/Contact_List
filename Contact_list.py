import json
class Contactlist:
    def __init__(self, path = "-"):
        self.contact_list = []
        if path != "-":
            print("Loading previous contacts...")
            with open(path, "r") as f:
                data = f.read()
                self.contact_list = json.loads(data)
            print("Loaded...")


    def add(self, name, number):
        self.contact_list.append({"Name": name, "Number":number })

    def search(self,name):
        result = []
        for item in self.contact_list:
            if name.lower() in item["Name"].lower():
                result.append(item)
        if result:
            print(f"Found contacts: {result}") 
        else:
            print(f"No results found for {name}")       

    def backup(self):
        with open("D:\\Python Übung\\Folge8\\backup\\contact_list.json", "w") as f:
           f.write(json.dumps(self.contact_list))
        print("Backup completed!")
    def print (self):
        print(f"Your contacts are: {self.contact_list}")


my_contact = Contactlist(path="D:\\Python Übung\\Folge8\\backup\\contact_list.json")
my_contact.print()