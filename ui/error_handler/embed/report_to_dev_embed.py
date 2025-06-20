import disnake
import traceback

def get(error: str) -> disnake.Embed:
    return disnake.Embed(
        title="📄 Детальний звіт помилки",
        color=disnake.Color.red()
    ).add_field(
        name=f"⚠️ - {str(error).split(":")[0]}",
        value=f"```\n{str(traceback.format_exception(error)).split("\\n")[-2]}\n```"
    ).set_footer(
        text=f"Детальний звіт про помилку надіслано розробнику. Виправлення буде виконано якнайшвидше."
    )