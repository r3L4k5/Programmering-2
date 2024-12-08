
import datetime as dt


class Task:                                                                                      
    def __init__(self, name: str, description: str = "", deadline: str = "", created: dt = dt.datetime.now().strftime('%d/%m-%Y %H:%M')) -> None:
        
        self.name = name
        self.created = created #Assigns time of creation, timezone accounted 
        self.deadline = deadline 
        self.description = description

        if deadline == "":
            self.deadline = "None"
        
    def __str__(self) -> str:
        return self.name
    
    def __dir__(self) -> dict[str]:
        return self.name, self.description, self.deadline, self.created    

    
    
    
