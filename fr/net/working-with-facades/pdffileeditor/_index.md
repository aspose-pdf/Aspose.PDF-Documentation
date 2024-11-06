---
title: PdfFileEditor Class
type: docs
weight: 10
url: fr/net/pdffileeditor-class/
description: Cette section explique comment travailler avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Travailler avec des documents PDF comprend diverses fonctions. La gestion des pages d'un fichier PDF est une partie importante de ce travail. Aspose.PDF.Facades fournit la classe `PdfFileEditor` à cette fin.

La classe PdfFileEditor contient les méthodes qui aident à manipuler des pages individuelles ; cette classe n'édite pas ou ne manipule pas le contenu d'une page. Vous pouvez insérer une nouvelle page, supprimer une page existante, diviser les pages ou vous pouvez spécifier l'imposition des pages en utilisant PdfFileEditor.

Les fonctionnalités fournies par cette classe peuvent être divisées en trois catégories principales, à savoir Édition de fichier, Imposition PDF, et Division. Nous allons discuter de ces sections en détail ci-dessous :

## Édition de fichier

Les fonctionnalités que nous pouvons inclure dans cette section sont Insérer, Ajouter, Supprimer, Concaténer et Extraire. You can insert a new page at a specified location using Insert method, or append the pages at the end of the file. You can also delete any number of pages from the file using Delete method, by specifying an integer array containing the numbers of pages to be deleted. Concatenate method helps you to join pages from multiple PDF files. You can extract any number of pages using Extract method, and save these pages into another PDF file or memory stream.

Vous pouvez insérer une nouvelle page à un emplacement spécifié en utilisant la méthode Insert, ou ajouter les pages à la fin du fichier. Vous pouvez également supprimer un nombre quelconque de pages du fichier en utilisant la méthode Delete, en spécifiant un tableau d'entiers contenant les numéros des pages à supprimer. La méthode Concatenate vous aide à joindre des pages de plusieurs fichiers PDF. Vous pouvez extraire un nombre quelconque de pages en utilisant la méthode Extract, et enregistrer ces pages dans un autre fichier PDF ou un flux de mémoire.

This section explores the capabilities of this class and explains the purpose of its methods.

Cette section explore les capacités de cette classe et explique le but de ses méthodes.

- [Concatenate PDF documents](/pdf/net/concatenate-pdf-documents/)
- [Extract PDF pages](/pdf/net/extract-pdf-pages/)
- [Insert PDF pages](/pdf/net/insert-pdf-pages/)
- [Delete PDF pages](/pdf/net/delete-pdf-pages/)

- [Concaténer des documents PDF](/pdf/net/concatenate-pdf-documents/)
- [Extraire des pages PDF](/pdf/net/extract-pdf-pages/)
- [Insérer des pages PDF](/pdf/net/insert-pdf-pages/)
- [Supprimer des pages PDF](/pdf/net/delete-pdf-pages/)

## Using Page Brakes

## Utilisation des sauts de page

Page Break is a special feature that allows to reflow of the document.

Le saut de page est une fonctionnalité spéciale qui permet de réorganiser le document.

- [Page Break in existing PDF](/pdf/net/page-break-in-existing-pdf/)

- [Saut de page dans un PDF existant](/pdf/net/page-break-in-existing-pdf/)

## PDF Imposition

## Imposition PDF

Imposition is the process of arranging pages correctly prior to printing.

L'imposition est le processus d'organisation correcte des pages avant l'impression. `PdfFileEditor` fournit deux méthodes à cet effet, c'est-à-dire `MakeBooklet` et `MakeNUp`. La méthode MakeBooklet aide à arranger les pages de sorte qu'il soit facile de les plier ou de les relier après impression, cependant, la méthode MakeNUp permet d'imprimer plusieurs pages sur une seule page du fichier PDF.

- [Créer un livret PDF](/pdf/net/make-booklet-of-pdf/)
- [Créer un NUp de fichiers PDF](/pdf/net/make-nup-of-pdf-files/)

## Fractionnement

La fonction de fractionnement vous permet de diviser un fichier PDF existant en différentes parties. Vous pouvez soit diviser la partie avant du fichier PDF, soit la partie arrière. Comme PdfFileEditor fournit une variété de méthodes pour les besoins de fractionnement, vous pouvez également diviser un fichier en pages individuelles ou en plusieurs ensembles de pages multiples.

- [Diviser les pages PDF](/pdf/net/split-pdf-pages/)