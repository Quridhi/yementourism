from flet import *
def main(page:Page):
    page.window.width=250
    page.window.title_bar_hidden=True
    page.window.height=470
    page.theme_mode=ThemeMode.DARK
    page.add(Text(value="مرحبا بك "),
             Text(value="welcome"),
             Image(src="images/my-logo.png")
             )

    def route_change(route):
        page.views.clear()


        page.views.append(
            View(
               "/",
               [
                   Text("first page"),
                   ElevatedButton("معالم يمنية",on_click=lambda _: page.go("/places")),
                   ElevatedButton("مدن يمنية",on_click=lambda _: page.go("/cities")),
                   ElevatedButton("تأريخ اليمن",on_click=lambda _: page.go("/history")),
                    ElevatedButton("About App",on_click=lambda _: page.go("/info"))
               ] 

            )
        )
        if page.route=="/places":
             page.views.append(
            View(
               "/places",
               [
                   Text("معالم في اليمن")
               ] 

            )
        )

        if page.route=="/cities":
             page.views.append(
            View(
               "/cities",
               [
                   Text("مدن يمنية")
               ] 

            )
        )
             
        
        if page.route=="/history":
             page.views.append(
            View(
               "/history",
               [
                   Text("تأريخ اليمن")
               ] 

            )
        )
        
        if page.route=="/info":
             page.views.append(
            View(
               "/info",
               [
                   Image(src="images/my-logo.png")
               ] 

            )
        )
             
        

        

        page.update()
    page.on_route_change=route_change
    page.go(page.route)

app(main)