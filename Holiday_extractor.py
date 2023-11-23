import pandas as pd
import requests
import customtkinter
import tkinter
from tkinter.filedialog import askopenfilenames


def run_app():
    try:
        if country_selector.get() == "Select country":
            tkinter.messagebox.showwarning(title="Warning", message="Please select country.")
            return
        elif len(entry_sample.get()) == 0:
            tkinter.messagebox.showwarning(title="Warning", message="Year field is missing. Please add year.")
            return
        elif format_selector.get() == "Select format":
            tkinter.messagebox.showwarning(title="Warning", message="Please select file extension.")
            return
        else:

            # Zdefiniuj URL API i kraj (np. Polska i rok 2023)
            api_url = "https://date.nager.at/api/v2/PublicHolidays"
            country_code = country_selector.get()
            year = int(entry_sample.get())
            file_extension = format_selector.get()
            # Utwórz pełny URL z parametrami
            full_url = f"{api_url}/{year}/{country_code}"

            # Wykonaj zapytanie GET do API
            response = requests.get(full_url)

            # Sprawdź, czy zapytanie zakończyło się sukcesem (kod 200)
            if response.status_code == 200:
                holidays_data = response.json()

                df = pd.DataFrame(holidays_data)

                if file_extension == 'xlsx':
                    output_file = f'Holiday {country_code} {year}.{file_extension}'
                    df.to_excel(r'Output/' + output_file, index=False)
                    tkinter.messagebox.showinfo(title="Updated", message="Results has been saved in the file.")

                else:
                    output_file = f'Holiday {country_code} {year}.{file_extension}'
                    df.to_csv(r'Output/' + output_file, index=False)
                    tkinter.messagebox.showinfo(title="Updated", message="Results has been saved in the file.")

            else:
                # W przypadku błędu, wydrukuj kod błędu
                print(f"Błąd {response.status_code}: {response.text}")

            

    except Exception as e:
        tkinter.messagebox.showerror('Error', str(e))           



# ============== Application ============
customtkinter.set_appearance_mode('white')
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("480x480")
app.title("CalendarCrafter")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=40, padx=60, fill="both", expand=True)


label = customtkinter.CTkLabel(master=frame_1, text="CalendarCrafter", font=("Roboto", 24), justify=customtkinter.LEFT)
label.pack(pady=10, padx=10)

run_button = customtkinter.CTkButton(master=frame_1, text="Run app", fg_color=("#A663CC"),hover_color=("#65B891"), command=run_app)
run_button.pack(pady=10, padx=10)

country_selector = customtkinter.CTkOptionMenu(frame_1, values=["PL", "NL", "TR", "IT", "ES", "SE", "BE"], fg_color=("#4381C1", "#3B6064"))
country_selector.pack(pady=10, padx=10)
country_selector.set("Select country") 

label_2 = customtkinter.CTkLabel(master=frame_1, text="Year", font=("Roboto", 20), justify=customtkinter.LEFT)
label_2.pack(pady=10, padx=10)

entry_sample = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter year")
entry_sample.pack(pady=20, padx=10)

label_3 = customtkinter.CTkLabel(master=frame_1, text="File extension", font=("Roboto", 20), justify=customtkinter.LEFT)
label_3.pack(pady=10, padx=10)

format_selector = customtkinter.CTkOptionMenu(frame_1, values=["csv", "xlsx"], fg_color=("#4381C1"), command=run_app)
format_selector.pack(pady=10, padx=10)
format_selector.set("Select format") 
 
        
app.mainloop()