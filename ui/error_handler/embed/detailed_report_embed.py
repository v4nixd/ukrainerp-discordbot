import disnake
import traceback

def get(error: str) -> disnake.Embed:
    return disnake.Embed(
        title="📄 Детальний звіт помилки",
        color=disnake.Color.red()
    ).add_field(
        name=f"⚠️ - {str(error).split(":")[0]}",
        value=f"```\n{str(traceback.format_exception(error))[-1000:]}\n```"
    ).set_footer(
        text=f"Натисніть кнопку нижче, якщо бажаєте повідомити розробнику про цю помилку."
    )