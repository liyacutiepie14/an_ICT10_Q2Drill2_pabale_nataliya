from js import document
import html

region1 = {"Liya Pabale", "Guia Florez", "Loriz Herrington"}
region2 = {"Ryle Suarez", "Mark Santos", "Mischa Joson", "Bonniered Decierto"}
region3 = {"Deion Deleon", "Sean Manaloto", "Megan Tanglao", "Carlos Narciso"}
region4 = {"Briella Basilio", "Tori Manalansan", "Venice Davinci", "Jem Castro"}


def show_members():
    all_members = set(region1) | set(region2) | set(region3) | set(region4)
    member_list = sorted(all_members)
    names = "<br>".join(html.escape(name) for name in member_list)

    document.getElementById("output").innerHTML = (
        "<h3>Updated Club Members</h3>" + names
    )


def add_member(event):
    global region1, region2, region3, region4

    first = document.getElementById("fname").value.strip()
    last = document.getElementById("lname").value.strip()

    full_name = f"{first} {last}".strip()
    if not full_name:
        return

    region1 = region1 | {full_name}
    show_members()

    document.getElementById("fname").value = ""
    document.getElementById("lname").value = ""


show_members()