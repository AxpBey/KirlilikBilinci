from email.mime import image
from http import client
from nturl2path import url2pathname
from sys import prefix
import discord, os, random, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "", intents = intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak girdik !')

@bot.command()
async def kirlilik_hakkında_bilgi_ver(ctx):
    await ctx.send(f'Tabi ki, Çevre kirliliği, çeşitli insan faaliyetleri ve doğal olaylar sonucunda çevre üzerinde olumsuz etkiler yaratan kirleticilerin (zehirli maddelerin, atıkların, gazların, kimyasalların, vb.) çevreye salınması sonucu meydana gelen çevresel bir sorundur. Çevre kirliliği, su, hava, toprak ve biyolojik sistemlerde olabilir. ')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Size nasıl yardımcı olabilirim ?')

@bot.command()
async def nasılsın(ctx):
    await ctx.send(f'Ben bir yazı robotu olduğum için benim duygularım yok :)') 

@bot.command()
async def çevre_kirliliği_nasıl_önlenir(ctx):
    await ctx.send(f'Geri Dönüşüm: Atıklarınızı geri dönüştürerek kaynakları koruyabilirsiniz. Kağıt, cam, plastik ve metal gibi malzemeleri geri dönüşüm tesislerine teslim edin.Enerji Verimliliği: Daha verimli enerji kullanımı, enerji kaynaklarını korur ve hava kirliliğini azaltır. Evde ve işyerinde enerji tasarrufu sağlamak için LED ampuller, izolasyon ve enerji verimli cihazlar kullanabilirsiniz.Temiz Enerji Kaynakları: Fosil yakıtların kullanımını azaltarak ve yenilenebilir enerji kaynaklarına yatırım yaparak enerji üretimini çevre dostu hale getirebilirsiniz.Su Tasarrufu: Su kaynaklarını korumak için duş alırken, muslukları kapatırken ve su sızıntılarını gidererek su tasarrufu yapın.Kimyasal Atıklar: Zararlı kimyasalları ve ilaçları uygun bir şekilde imha edin. Kimyasal atıkları sızıntılara karşı korumak için gerekli önlemleri alın.Havalandırma ve Ulaşım: Araç kullanımını sınırlayın ve toplu taşımayı veya bisikleti tercih edin. Ayrıca daha az sera gazı emisyonuna neden olan araçlara yatırım yapın.Orman Koruma: Ormanların korunması, karbon emisyonlarının azaltılması ve biyoçeşitliliğin korunması için önemlidir.Atık Yönetimi: Atık miktarını azaltmak ve atıkları uygun şekilde bertaraf etmek için geri dönüşüm ve kompost yapımı gibi atık yönetimi uygulamalarını benimseyin.Sürdürülebilir Tarım ve Balıkçılık: Sürdürülebilir tarım ve balıkçılık uygulamaları, toprak ve su kaynaklarını korurken gıda üretimini destekler.Eğitim ve Bilinçlendirme: Çevre sorunları hakkında toplumu bilinçlendirmek ve eğitmek, kirliliği önlemek için önemlidir. İnsanların çevre bilinci geliştirmelerine yardımcı olun.Yasal Düzenlemeler: Hükümetler ve yerel otoritelerin çevre koruma yasalarını uygulamalarını ve çevre kirliliğini sınırlamalarını teşvik edin.')




@bot.command()
async def kirlilik_türleri_kaç_tanedir(ctx):
    await ctx.send(f"Hava Kirliliği: Atmosferde zararlı gazlar, partiküller ve kimyasalların yüksek miktarlarda bulunmasıdır. Örneğin, hava kirliliği egzoz gazları, endüstriyel emisyonlar ve yanıcı fosil yakıtların kullanımı nedeniyle oluşabilir.Su Kirliliği: Suların nehirler, göller, okyanuslar kirletilmesidir. Sanayi atıkları, tarım ilaçları, evsel atıklar, petrol sızıntıları ve diğer kimyasallar su kaynaklarına yayıldığında su kirliliği oluşur.Toprak Kirliliği: Toprakların zararlı kimyasallarla veya kirleticilerle kontamine edilmesidir. Kimyasal atıkların yeraltı sularına sızması veya kimyasalların toprakta birikmesi, toprak kirliliğine neden olur.Gürültü Kirliliği: Fazla gürültü seviyelerinin insan sağlığına veya çevreye olumsuz etkileri olduğunda meydana gelir. İnşaat faaliyetleri, trafik, fabrika gürültüsü gibi kaynaklardan kaynaklanabilir.Işık Kirliliği: Yüksek ışık seviyelerinin geceleyin çevre üzerinde yarattığı olumsuz etkilere işaret eder. Bu tür kirliliğin nedeni, aşırı aydınlatma ve ışık kaynaklarının yanlış kullanımı olabilir.Radyasyon Kirliliği: Radyoaktif maddelerin nükleer santrallerden veya nükleer kazalardan sızması sonucu ortaya çıkan bir tür kirliliktir.")


bot.run("YOUR BOT TOKEN")
