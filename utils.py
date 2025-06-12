import disnake

from logger import logger

def getRole(guild: disnake.Guild, role_id: int) -> disnake.Role | None:
    role = guild.get_role(role_id)

    if role is None:
        logger.error(f"Role with id `{role_id}` not found in guild `{guild.id}`")
    
    return role