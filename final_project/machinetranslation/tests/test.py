from asyncio.windows_events import NULL
from translator import englishToFrench, frenchToEnglish


print("\n English to French NULL: ",englishToFrench(NULL))
print("\n French to English NULL: ",frenchToEnglish(NULL))

print("\n English to French: ",englishToFrench('Hello'))
print("\n French to English: ",frenchToEnglish('Bonjour'))
