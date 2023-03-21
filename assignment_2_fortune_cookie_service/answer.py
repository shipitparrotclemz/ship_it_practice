import random


class CookieService:
    def  __init__(self, cookies: list[str]):
        self.cookies = cookies

    # Q: Is this a static method? or is this an instance method?
    # A: instance
    # Q: Why?
    # A: because there is self!
    # to be specific, the implementation of get_cookie uses self.cookies
    def get_cookie(self) -> str:
        return random.choice(self.cookies)


# Rule of thumb:
# If a value associated with a class doesn't change much, it can be placed as an attribute
# Q: Cookies don't change much. should it be an attribute of CookieService?
# A: YES!

if __name__ == "__main__":
    cookies: list[str] = [
        "You will soon embark on a great adventure.",
        "A lifetime of happiness lies ahead of you.",
        "Good things come to those who wait.",
        "You will receive unexpected good news.",
        "Your hard work will pay off in the end.",
        "You will make a lifelong friend very soon.",
        "You will find success in all your endeavors.",
        "Your future looks very bright.",
        "Your creativity will lead to great success.",
        "You will find true love very soon.",
        "Your kindness will be repaid many times over.",
        "Your financial situation will greatly improve.",
        "You will achieve your dreams and goals.",
        "You will be blessed with good luck.",
        "Your future is full of promise and opportunity.",
        "Your intelligence will be recognized and rewarded.",
        "You will overcome any obstacle in your path.",
        "You will make a positive difference in the world.",
        "Your inner strength will guide you to success.",
        "You will receive a promotion or raise soon.",
        "Your talents will be put to good use.",
        "Your journey will be filled with happiness.",
        "You will meet someone very special soon.",
        "Your hard work and dedication will pay off.",
        "You will be successful in all your endeavors.",
        "Your life is full of love and happiness.",
        "You will find peace and contentment in your life.",
        "Your future is looking bright and sunny.",
        "You will make a significant impact on the world.",
        "Your dreams will come true.",
        "You will be recognized for your achievements.",
        "Your life is filled with abundance and prosperity.",
        "You will have a long and happy life.",
        "Your health will improve significantly.",
        "You will find great joy in the little things in life.",
        "You will be surrounded by love and support.",
        "Your future is full of possibilities.",
        "You will find success in everything you do.",
        "You will have a happy and fulfilling life.",
        "You will be surrounded by beauty and grace.",
        "Your life is a reflection of your thoughts and actions.",
        "You will achieve great things in your life.",
        "You will find happiness in the simple things.",
        "You will be blessed with good health and vitality.",
        "Your spirit is strong and unbreakable.",
        "You will find success in unexpected ways.",
        "Your life will be filled with love and laughter.",
        "You will find true happiness in your relationships.",
        "Your future is filled with endless possibilities.",
        "You will find strength in times of adversity.",
        "Your dreams are within your reach.",
        "You will be surrounded by positive energy.",
        "Your life is a canvas waiting to be painted.",
        "You will find peace in your heart.",
        "Your future is full of excitement and adventure.",
        "You will find happiness in your career.",
        "Your life is filled with love and joy.",
        "You will be successful in all your endeavors.",
        "Your heart is open to new possibilities.",
        "You will find love and happiness with someone special.",
        "Your future is full of prosperity and abundance.",
        "You will find inspiration in the world around you.",
        "Your spirit is filled with light and hope.",
        "Your dreams will lead you to great success.",
        "You will find happiness in the journey.",
        "Your life is filled with wonder and awe.",
        "You will be surrounded by positive people.",
        "Your future is bright and full of possibilities.",
        "You will find success and fulfillment in your work.",
    ]

    cookie_service: CookieService = CookieService(cookies=cookies)

    print(cookie_service.get_cookie())



