from animal import animal


class cat(animal):
    """
    안녕 정근원
    """
    
    def cry(self):
        """
        안녕 정근원 크라이함수야
        """
        return "나는 리턴해서 받아오기때문에 늦게 생성되"

    def __str__(self):
        return self.name

c = cat("내가 먼저실행되고")

print(c)
print(c.cry())


