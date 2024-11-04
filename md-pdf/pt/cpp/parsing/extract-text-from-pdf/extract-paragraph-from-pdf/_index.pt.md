---
title: Extrair Parágrafo do PDF 
linktitle: Extrair Parágrafo do PDF 
type: docs 
weight: 20 
url: /cpp/extract-paragraph-from-pdf/ 
description: Este artigo descreve como usar o ParagraphAbsorber - uma ferramenta especial no Aspose.PDF para extrair texto de documentos PDF. 
lastmod: "2021-12-13" 
sitemap: 
    changefreq: "weekly" 
    priority: 0.7 
---

## Extrair Texto do documento PDF em forma de Parágrafos

Podemos obter texto de um documento PDF pesquisando um texto específico (usando "texto simples" ou "expressões regulares") de uma única página ou de todo o documento, ou podemos obter o texto completo de uma única página, intervalo de páginas ou documento completo. No entanto, em alguns casos, você precisa extrair parágrafos de um documento PDF ou texto na forma de parágrafos. Implementamos a funcionalidade para pesquisar seções e parágrafos no texto das páginas do documento PDF. Introduzimos a Classe ParagraphAbsorber (como TextFragmentAbsorber e TextAbsorber), que pode ser usada para extrair parágrafos de documentos PDF. Existem duas maneiras a seguir nas quais você pode usar ParagraphAbsorber:

```cpp
static void DrawRectangleOnPage(System::SmartPtr<Rectangle> rectangle, System::SmartPtr<Page> page);
static void DrawPolygonOnPage(System::ArrayPtr<System::SmartPtr<Point>> polygon, System::SmartPtr<Page> page);
void Parsing::ExtractParagraph()
{
    // O caminho para o diretório dos documentos.
    std::clog << __func__ << ": Start" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    auto doc = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = doc->get_Pages()->idx_get(1);

    auto absorber = MakeObject<ParagraphAbsorber>();
    absorber->Visit(page);

    auto markup = absorber->get_PageMarkups()->idx_get(0);

    for(auto &section : markup->get_Sections())
    {
        DrawRectangleOnPage(section->get_Rectangle(), page);
        for(auto &paragraph : section->get_Paragraphs())
        {
        DrawPolygonOnPage(paragraph->get_Points(), page);
        }
    }

    doc->Save(_dataDir + u"output_out.pdf");
}

void DrawRectangleOnPage(System::SmartPtr<Rectangle> rectangle, System::SmartPtr<Page> page)
{
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 0, 0));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::SetRGBColorStroke>(0, 1, 0));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::SetLineWidth>(2));
    page->get_Contents()->Add(
        MakeObject<Aspose::Pdf::Operators::Re>(
        rectangle->get_LLX(),
        rectangle->get_LLY(),
        rectangle->get_Width(),
        rectangle->get_Height()));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ClosePathStroke>());
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
}

void DrawPolygonOnPage(System::ArrayPtr<System::SmartPtr<Point>> polygon, System::SmartPtr<Page> page)
{
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 0, 0));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::SetRGBColorStroke>(0, 0, 1));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::SetLineWidth>(1));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::MoveTo>(polygon->idx_get(0)->get_X(), polygon[0]->get_Y()));
    for (int i = 1; i < polygon->get_Length(); i++)
    {
        page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::LineTo>(polygon->idx_get(i)->get_X(), polygon[i]->get_Y()));
    }
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::LineTo>(polygon->idx_get(0)->get_X(), polygon[0]->get_Y()));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ClosePathStroke>());
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
}
```