---
title: Comment Créer un Portfolio PDF
type: docs
weight: 10
url: /java/how-to-create-pdf-portfolio/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Les portfolios PDF vous permettent de réunir du contenu provenant de diverses sources (par exemple, des fichiers PDF, Word, Excel, JPEG) dans un conteneur unique. Les fichiers originaux conservent leur identité individuelle mais sont assemblés dans un fichier portfolio PDF. Les utilisateurs peuvent ouvrir, lire, éditer et formater chaque fichier composant indépendamment des autres fichiers composants.

Aspose.PDF pour Java permet la création de documents de portfolio PDF en utilisant la classe Document. Chargez le fichier individuel dans un objet FileSpecification et ajoutez-les à l'objet Document.Collection en utilisant la méthode add(...). Une fois les fichiers ajoutés, utilisez la méthode save(..) de la classe Document pour générer le document portfolio.

{{% /alert %}}

## Exemple de Code

L'exemple suivant utilise un fichier Microsoft XPS, un document Word, un PDF et un fichier image pour créer un portfolio PDF.

**Un portfolio PDF créé avec Aspose.PDF**

![todo:image_alt_text](how-to-create-pdf-portfolio_1.png)

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "CreatePDFPortfolio.java" >}}