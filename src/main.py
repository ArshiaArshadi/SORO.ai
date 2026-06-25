from backup_manager import create_safe_backup
import filters
from tkinter import filedialog, simpledialog, messagebox, Tk


def main():
    # hide the main blank tkinter window
    root = Tk()
    root.withdraw()

    # open graphical window to select folder
    user_path = filedialog.askdirectory(title=" Select Folder to Organize ")

    # handle case where user cancels folder selection
    if not user_path:
        messagebox.showwarning("Cancelled", "No folder selected. Exiting...")
        return

    cleaned_path = user_path.strip()

    # prepare menu text for the dialog box
    menu_text = (
        "--- Select ONE filter to apply ---\n\n"
        "1. Filter by Extension (Documents, Images, etc.)\n"
        "2. Filter by Size (Isolate heavy files)\n"
        "3. Filter by Timeline (Archive by Year/Month)\n\n"
        "Enter your choice (1-3):"
    )    
    # open graphical input box to get user choice
    choice = simpledialog.askstring("Filter Menu", menu_text)

    # handle case where user cancels the menu dialog
    if not choice:
        messagebox.showwarning("Cancelled", "No filter selected. Exiting...")
        return
        
    choice = choice.strip()

    # phase 1: create safe backup of the folder
    organized_folder_path = create_safe_backup(cleaned_path)

    # phase 2: apply the selected filter
    if organized_folder_path:
        # check user choice and run the specific filter
        if choice == "1":
            filters.filter_by_extension(organized_folder_path)
            messagebox.showinfo("Success", "Extension filtering completed!")
        elif choice == "2":
            filters.filter_by_size(organized_folder_path, size_limit_mb=10)
            messagebox.showinfo("Success", "Size filtering completed!")
        elif choice == "3":
            filters.filter_by_timeline(organized_folder_path)
            messagebox.showinfo("Success", "Timeline archive completed!")
        else:
            # handle invalid choice with graphical warning
            messagebox.showwarning("Warning", "Invalid choice. No filters were applied.")
            
        # show final success message box
        messagebox.showinfo("Done", f"Customized organization is done!\nResult: {organized_folder_path}")
    else:
        # show graphical error message if backup fails
        messagebox.showerror("Error", "Operation failed. Please check the path.")


if __name__ == "__main__":
    main()