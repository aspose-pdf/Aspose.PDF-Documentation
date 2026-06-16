---
title: Extraire le texte d'un PDF - Facades
type: docs
weight: 10
url: /fr/cpp/extract-text-from-pdf-facades/
---

## <ins>**Extraire le texte de toutes les pages du document**
Afin d'extraire le texte de toutes les pages du document PDF, **Aspose.PDF pour C++** propose la classe PdfExtractor sous l'espace de noms Facades. Vous pouvez extraire tout le texte du document PDF, le sauvegarder dans un objet MemoryStream et l'obtenir sous forme de chaîne, au cas où vous souhaiteriez l'utiliser pour d'autres manipulations. Le code suivant vous montrera comment utiliser la classe PdfExtractor pour extraire le texte de toutes les pages du document PDF.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
auto extractor = MakeObject<Facades::PdfExtractor>();	
extractor->BindPdf(L"..\\Data\\Text\\input.pdf");
extractor->ExtractText();
	
auto memStream = MakeObject<IO::MemoryStream>();
extractor->GetText(memStream);

auto unicode = System::Text::Encoding::get_Unicode();

String allText = unicode->GetString(memStream->ToArray());	
Console::WriteLine(allText);
```