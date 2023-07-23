class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.protection = 0

        self.power += knight_config["weapon"]["power"]

        if knight_config["armour"]:
            for armour_parts in knight_config["armour"]:
                self.protection += armour_parts["protection"]

        if knight_config["potion"]:
            self.power += knight_config["potion"]["effect"].get("power", 0)
            self.hp += knight_config["potion"]["effect"].get("hp", 0)
            self.protection += (
                knight_config["potion"]["effect"].get("protection", 0)
            )
