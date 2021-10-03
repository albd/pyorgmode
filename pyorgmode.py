from datetime import datetime

class OrgLink:
    def __init__(self, title, url) -> None:
        self.title = title
        self.url = url
    
    def __str__(self) -> str:
        return f'[[{self.url}][{self.title}]]'

class OrgDate:
    def __init__(self, date: datetime) -> None:
        self.date : datetime = date

    def __str__(self) -> str:
        return f'[{self.date.strftime("%Y-%m-%d %a %H:%M")}]'

class OrgString:
    def __init__(self, strlist) -> None:
        if isinstance(strlist, str):
            self.items = [str]
        self.items = strlist

    def __str__(self) -> str:
        return ''.join(str(item) for item in self.items)

    def get_dates(self):
        raise NotImplementedError

    def get_links(self):
        raise NotImplementedError

class OrgHeading:
    def __init__(self, heading="", body="", tags=None) -> None:
        self.heading : OrgString = heading
        self.body: OrgString = body
        self.tags: List[str] = tags if tags else []
        self.depth = 1
        self.subheadings : List[OrgHeading] = []
    
    def append_subheading(self, heading: "OrgHeading"):
        heading.depth = self.depth + 1
        self.subheadings.append(heading)

    def tagline(self) -> str:
        if self.tags:
            return f" :{':'.join(self.tags)}:"
        else:
            return ''

    def headline(self) -> str:
        return f"{'*'*self.depth} {self.heading}{self.tagline()}"
        
    def __str__(self) -> str:
        ret = ""
        ret += self.headline()
        if self.body:
            ret += '\n' + str(self.body)
        for subheading in self.subheadings:
            ret+= '\n' + str(subheading)
        return ret

class OrgFile:
    def __init__(self) -> None:
        self.headings = []
    
    def append_heading(self, heading):
        self.headings.append(heading)
    
    def __str__(self) -> str:
        return '\n'.join(str(heading) for heading in self.headings)


#top = OrgFile()
#world = OrgHeading("world")
#world.tags.append('tag1')
#world.tags.append('tag2')
#top.append_heading(world)
#universe = OrgHeading("universe")
#world.append_heading(universe)
#universe.body = "hahamuhaah"
#world.body = "gomorrah"
#print(top)

od = OrgDate(datetime.now())
print(od)