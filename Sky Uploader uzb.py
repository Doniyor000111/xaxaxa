from .. import loader, utils
import siaskynet as skynet
import os

@loader.tds
class SkynetUploaderMod(loader.Module):
    """siasky.net uploader"""
    strings = {"name": "SkynetUploader"}

    async def skycmd(self, message):
        """ .sky <faylga takrorlash> - faylni xostga yuklaydi
         yoki
         .sky <matnni takrorlash> - matnni takrorlashdan xostga yuklaydi
        """
        await message.edit(f"<b>Yuklash...</b>")
        client = skynet.SkynetClient()
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("Faylga javob bering!")
            return
        try:
            file = await reply.download_media()
            link = client.upload_file(file)
            filtered = link.split('sia://')
            link = 'https://siasky.net/' +  str(filtered[1])
            await message.edit("Havola: \n" + link)
        except:
            f = open('text.txt', 'w')
            f.write(reply.raw_text)
            f.close()
            link = client.upload_file("text.txt")
            filtered = link.split('sia://')
            link = 'https://siasky.net/' +  str(filtered[1])
            await message.edit("Линк: \n" + link)
            os.remove('text.txt')
Sssssssss
