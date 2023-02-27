

# Dataclass Intro: https://www.infoworld.com/article/3563878/how-to-use-python-dataclasses.html

from dataclasses import dataclass, astuple, asdict, field

@dataclass
class Comment:
    '''Just another class.'''
    id: int 
    weight: float = field(default=0.0)
    title: str = field(default="")
    page: int = field(default=0)


comment1 = Comment(id=1, title=str(1), page=1)

print(comment1.id)
print(comment1.title)
print(comment1.page)

print(str(comment1))

quit()
