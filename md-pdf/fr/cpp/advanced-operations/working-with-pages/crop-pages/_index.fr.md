---
title: Recadrer les pages PDF par programmation C++
linktitle: Recadrer les pages
type: docs
weight: 80
url: /cpp/crop-pages/
description: Vous pouvez obtenir les propriétés de la page, telles que la largeur, la hauteur, le bleed-, crop- et trimbox en utilisant Aspose.PDF pour C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir les propriétés de la page

Chaque page d'un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, le bleed-, crop- et trimbox. Aspose.PDF vous permet d'accéder à ces propriétés.

- **Mediabox**: La mediabox est la plus grande boîte de page. Elle correspond à la taille de la page (par exemple A4, A5, US Letter, etc.) sélectionnée lorsque le document a été imprimé en PostScript ou PDF. En d'autres termes, la mediabox détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **Boîte de rognage**: Si le document a un rognage, le PDF aura également une boîte de rognage. Bleed est la quantité de couleur (ou d'œuvre) qui s'étend au-delà du bord d'une page. Il est utilisé pour s'assurer que lorsque le document est imprimé et coupé à la taille ("rogné"), l'encre ira jusqu'au bord de la page. Même si la page est mal coupée - coupée légèrement en dehors des marques de coupe - aucun bord blanc n'apparaîtra sur la page.
- **Trim box**: La boîte de rognage indique la taille finale d'un document après impression et rognage.
- **Art box**: La boîte d'art est la boîte dessinée autour du contenu réel des pages de vos documents. Cette boîte de page est utilisée lors de l'importation de documents PDF dans d'autres applications.
- **Crop box**: La boîte de coupe est la taille "page" à laquelle votre document PDF est affiché dans Adobe Acrobat. En vue normale, seul le contenu de la boîte de coupe est affiché dans Adobe Acrobat. Pour des descriptions détaillées de ces propriétés, lisez la spécification Adobe.Pdf, en particulier 10.10.1 Page Boundaries.
- **Page.Rect**: l'intersection (rectangle visible commun) du MediaBox et du DropBox. La photo ci-dessous illustre ces propriétés.  
Pour plus de détails, veuillez visiter [cette page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

Le snippet ci-dessous montre comment recadrer la page :

```cpp
void CropPagesPDF()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("crop_page.pdf");
    String outputFileName("crop_page_out.pdf");

    // Open source document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    Console::WriteLine(document->get_Pages()->idx_get(1)->get_CropBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_TrimBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_ArtBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_BleedBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_MediaBox());

    // Create new Box Rectagle
    auto newBox = MakeObject<Rectangle>(200, 220, 2170, 1520);
    document->get_Pages()->idx_get(1)->set_CropBox(newBox);
    document->get_Pages()->idx_get(1)->set_TrimBox(newBox);
    document->get_Pages()->idx_get(1)->set_ArtBox (newBox);
    document->get_Pages()->idx_get(1)->set_BleedBox (newBox);

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```
In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.  
![Figure 1. Cropped Page](crop_page.png)

Après la modification, la page ressemblera à la Figure 2.  
![Figure 2. Cropped Page](crop_page2.png)