class page():
    def __init__ (self, max_pages:int) -> None:
        self.current_page:int = 1
        self.max_pages = max_pages


        self.display:str = self._build_pagination()

    def pagination_action (self, action) -> None:
        if action == 'next' and self.current_page != self.max_pages:
            self.current_page += 1
        if action == 'previous' and self.current_page != 1:
            self.current_page -= 1
            
        self.display = self._build_pagination()

    def _build_pagination (self) -> str:

        if self.max_pages <= 7:
            output = []

            for i in range(1,self.max_pages+1):
                if i == self.current_page:
                    output.append(f'({i})')
                else:
                    output.append(str(i))
            
            return " ".join(output)
        
        elif self.current_page < 5:
            output = []

            for i in range(1,6):
                if i == self.current_page:
                    output.append(f'({i})')
                else:
                    output.append(str(i))
            
            lower =  " ".join(output)

            return f"{lower} ... {self.max_pages}"
        
        elif self.current_page > self.max_pages-5 and self.current_page >= 6:
            output = []

            for i in range(self.max_pages-4,self.max_pages+1):
                if i == self.current_page:
                    output.append(f'({i})')
                else:
                    output.append(str(i))
            
            upper =  " ".join(output)

            return f"1 ... {upper}"
        
        else:
            return f"1 ... {self.current_page-1} ({self.current_page}) {self.current_page+1} ... {self.max_pages}"
    

