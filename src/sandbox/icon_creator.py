import os
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def create_german_flag_icon(folder: Path, icon_size=256):
    # Define the colors
    black = (0, 0, 0)
    red = (255, 0, 0)
    gold = (255, 204, 0)

    # Create a new image with a white background
    flag_image = Image.new("RGB", (icon_size, icon_size), "white")
    draw = ImageDraw.Draw(flag_image)

    # Height of each stripe
    stripe_height = icon_size // 3

    # Draw the black stripe
    draw.rectangle([0, 0, icon_size, stripe_height], fill=black)

    # Draw the red stripe
    draw.rectangle([0, stripe_height, icon_size, 2 * stripe_height], fill=red)

    # Draw the gold stripe
    draw.rectangle([0, 2 * stripe_height, icon_size, icon_size], fill=gold)

    # Save the image as .ico file
    flag_image.save(folder / "german_flag.ico", format="ICO")


def create_circular_german_flag_icon(folder: Path, icon_size=256):
    # Define the colors
    black = (0, 0, 0)
    red = (255, 0, 0)
    gold = (255, 204, 0)

    # Create a new image with a transparent background
    flag_image = Image.new("RGBA", (icon_size, icon_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(flag_image)

    # Create a mask for the circular area
    mask = Image.new("L", (icon_size, icon_size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, icon_size, icon_size), fill=255)

    # Draw the flag colors within the circular area
    stripe_height = icon_size // 3

    # Draw the black stripe
    draw.rectangle([0, 0, icon_size, stripe_height], fill=black)

    # Draw the red stripe
    draw.rectangle([0, stripe_height, icon_size, 2 * stripe_height], fill=red)

    # Draw the gold stripe
    draw.rectangle([0, 2 * stripe_height, icon_size, icon_size], fill=gold)

    # Apply the circular mask
    flag_image.putalpha(mask)

    # Save the image as .ico file
    flag_image.save(folder / "circular_german_flag.ico", format="ICO")


def create_circular_italian_flag_icon(folder: Path, icon_size=256):
    # Define the colors
    green = (0, 146, 70)
    white = (255, 255, 255)
    red = (206, 43, 55)

    # Create a new image with a transparent background
    flag_image = Image.new("RGBA", (icon_size, icon_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(flag_image)

    # Create a mask for the circular area
    mask = Image.new("L", (icon_size, icon_size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, icon_size, icon_size), fill=255)

    # Draw the flag colors within the circular area
    stripe_width = icon_size // 3

    # Draw the green stripe
    draw.rectangle([0, 0, stripe_width, icon_size], fill=green)

    # Draw the white stripe
    draw.rectangle([stripe_width, 0, 2 * stripe_width, icon_size], fill=white)

    # Draw the red stripe
    draw.rectangle([2 * stripe_width, 0, icon_size, icon_size], fill=red)

    # Apply the circular mask
    flag_image.putalpha(mask)

    # Save the image as .ico file
    flag_image.save(folder / "circular_italian_flag.ico", format="ICO")


def create_circular_argentinian_flag_icon(folder: Path, icon_size=256):
    # Define the colors
    sky_blue = (116, 172, 223)
    white = (255, 255, 255)
    sun_yellow = (252, 209, 22)  # Color aproximado del Sol de Mayo

    # Crear imagen base transparente
    flag_image = Image.new("RGBA", (icon_size, icon_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(flag_image)

    # Crear máscara circular
    mask = Image.new("L", (icon_size, icon_size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, icon_size, icon_size), fill=255)

    # Altura de cada franja
    stripe_height = icon_size // 3

    # Dibujar franjas
    draw.rectangle([0, 0, icon_size, stripe_height], fill=sky_blue)
    draw.rectangle([0, stripe_height, icon_size, 2 * stripe_height], fill=white)
    draw.rectangle([0, 2 * stripe_height, icon_size, icon_size], fill=sky_blue)

    # Dibujar el "Sol de Mayo" como un círculo amarillo
    sun_diameter = int(icon_size * 0.25)  # 25% del tamaño total
    sun_radius = sun_diameter // 2
    sun_center_x = icon_size // 2
    sun_center_y = stripe_height + stripe_height // 2
    sun_bounds = [
        sun_center_x - sun_radius,
        sun_center_y - sun_radius,
        sun_center_x + sun_radius,
        sun_center_y + sun_radius,
    ]
    draw.ellipse(sun_bounds, fill=sun_yellow)

    # Aplicar máscara circular
    flag_image.putalpha(mask)

    # Guardar el ícono
    flag_image.save(folder / "circular_argentinian_flag.ico", format="ICO")


def create_circular_austrian_flag_icon(folder: Path, icon_size=256):
    # Colores
    red = (237, 41, 57)
    white = (255, 255, 255)

    # Imagen base con fondo transparente
    flag_image = Image.new("RGBA", (icon_size, icon_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(flag_image)

    # Máscara circular
    mask = Image.new("L", (icon_size, icon_size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, icon_size, icon_size), fill=255)

    # Altura de cada franja
    stripe_height = icon_size // 3

    # Franja roja superior
    draw.rectangle([0, 0, icon_size, stripe_height], fill=red)
    # Franja blanca central
    draw.rectangle([0, stripe_height, icon_size, 2 * stripe_height], fill=white)
    # Franja roja inferior
    draw.rectangle([0, 2 * stripe_height, icon_size, icon_size], fill=red)

    # Aplicar la máscara circular
    flag_image.putalpha(mask)

    # Guardar
    flag_image.save(folder / "circular_austrian_flag.ico", format="ICO")


def create_expynses_icon(folder: Path, icon_size=256):  # Colors
    folder_color = (255, 223, 0)  # Yellow for the folder
    financial_color = (0, 128, 0)  # Green for financial symbols

    # Create a new image with a transparent background
    icon_image = Image.new("RGBA", (icon_size, icon_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(icon_image)

    # Draw the folder shape
    folder_height = icon_size * 0.7
    tab_height = icon_size * 0.2
    tab_width = icon_size * 0.4
    draw.rectangle(
        [0, tab_height, icon_size, folder_height + tab_height], fill=folder_color
    )
    draw.rectangle([0, 0, tab_width, tab_height], fill=folder_color)

    # Draw financial symbol (dollar sign)
    font_size = int(icon_size * 0.5)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except OSError:
        font = ImageFont.load_default()
    text = "$"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = (
        (icon_size - text_width) // 2,
        (folder_height + tab_height - text_height) // 2,
    )
    draw.text(text_position, text, fill=financial_color, font=font)

    # Save the image as .ico file
    icon_image.save(folder / "family_finances_folder.ico", format="ICO")


def generate_rc_file(ico_folder: Path, rc_filename: str = "custom_icons.rc"):
    icon_files = [f for f in os.listdir(ico_folder) if f.endswith(".ico")]
    rc_path = ico_folder / rc_filename

    with rc_path.open("w") as rc:
        for i, icon in enumerate(icon_files, start=1):
            name = os.path.splitext(icon)[0].upper().replace(" ", "_")
            icon_path = (ico_folder / icon).resolve().as_posix()  # ← ABSOLUTO
            rc.write(f'{name} ICON "{icon_path}"\n')

    print(f"Archivo .rc generado: {rc_path}")


def build_icon_library(
    ico_folder: Path,
    output_name: str = "custom_icon_library.dll",
    target_folder: Path = Path("C:/Windows"),
):
    # Archivos intermedios
    rc_path = ico_folder / "flags.rc"
    res_path = ico_folder / "flags.res"
    dll_path = ico_folder / output_name
    final_path = target_folder / output_name

    # Generar archivo .rc
    generate_rc_file(ico_folder)
    windres_path = "C:/MinGW/bin/windres.exe"
    rc_abs = rc_path.resolve().as_posix()
    res_abs = res_path.resolve().as_posix()
    dll_abs = dll_path.resolve().as_posix()

    # Ejecutar windres
    print("\n--- EJECUTANDO windres ---")
    print(f"Comando: {windres_path} {rc_abs} -O coff -o {res_abs}\n")

    try:
        cmd = [windres_path, rc_abs, "-O", "coff", "-o", res_abs]
        print(f"\nEjecutando comando:\n{' '.join(cmd)}\n")
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("❌ Error ejecutando windres:")
        print(e)
        print("Sugerencias:")
        print(
            "- Asegurate de que el archivo flags.rc existe y tiene rutas ABSOLUTAS correctas."
        )
        print(
            "- Ejecutá manualmente ese mismo comando en Git Bash para ver el mensaje de error exacto.\n"
        )
        raise

    print("--- Compilando con gcc ---")
    subprocess.run(["gcc", "-shared", "-o", dll_abs, res_abs], check=True)

    print(f"Copiando DLL a: {final_path}")
    shutil.copy2(dll_path, final_path)
    print("✅ Librería de íconos instalada con éxito.")


if __name__ == "__main__":
    folder = Path("./icons")
    # create_german_flag_icon(folder=folder)
    # create_circular_german_flag_icon(folder=folder)
    # create_circular_italian_flag_icon(folder=folder)
    # create_expynses_icon(folder=folder)
    # create_circular_argentinian_flag_icon(folder=folder)
    create_circular_austrian_flag_icon(folder=folder)

    # Adds all the files in the folder to a compiled file
    generate_rc_file(ico_folder=folder, rc_filename="custom_icons.rc")

    # 1. Install MinGW with windres and gcc packages.
    # 2. Add MinGW to the PATH.
    # 3. Run from git bash:
    #      windres custom_icons.rc -O coff -o custom_icons.res
    #      gcc -shared -o custom_icons.dll custom_icons.res
    # 4. Do this with admin permissions (most likely, manually)
    # 5.   cp /c/git/sandbox/icons/custom_icons.dll /c/Windows/System32/

    # Automation:
    # build_icon_library(ico_folder=folder)  # NOT YET WORKING.
    # IT SEEMS AN ISSUE WITH THE PATHS. The same command outside Python (using MINGW) works fine.
