from django.test import TestCase

# Create your tests here.
FatBoss = type('FatBoss',(),{'hobby':"胖子老板卖槟榔"})
fat_boss = FatBoss()
print(fat_boss.hobby)