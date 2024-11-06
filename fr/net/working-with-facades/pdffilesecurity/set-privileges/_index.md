---
title: Définir des privilèges sur un PDF
type: docs
weight: 50
url: fr/net/set-privileges/
description: Ce sujet explique comment définir des privilèges sur un fichier PDF existant en utilisant la classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Définir des privilèges sur un fichier PDF existant

Pour définir les privilèges d'un fichier PDF, créez un objet [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) et appelez la méthode SetPrivilege. Vous pouvez spécifier les privilèges en utilisant l'objet DocumentPrivilege et ensuite passer cet objet à la méthode SetPrivilege. L'extrait de code suivant vous montre comment définir les privilèges d'un fichier PDF.

```csharp
public static void SetPrivilege1()
 {
    // Créez un objet DocumentPrivileges
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Créez un objet PdfFileSecurity
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

Voir la méthode suivante avec spécification d'un mot de passe :

```csharp
 public static void SetPrivilege2()
 {
    // Créer un objet DocumentPrivileges
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Créer un objet PdfFileSecurity
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

## Supprimer la fonctionnalité des droits étendus du PDF

Les documents PDF prennent en charge la fonctionnalité des droits étendus pour permettre à l'utilisateur final de remplir des données dans les champs de formulaire en utilisant Adobe Acrobat Reader, puis de sauvegarder une copie du formulaire rempli. Cependant, cela garantit que le fichier PDF n'est pas modifié et si une modification de la structure du PDF est effectuée, la fonctionnalité de droits étendus est perdue. Lors de la visualisation d'un tel document, un message d'erreur est affiché, indiquant que les droits étendus sont supprimés parce que le document a été modifié. Récemment, nous avons reçu une demande de suppression des droits étendus d'un document PDF.

Pour supprimer les droits étendus d'un fichier PDF, une nouvelle méthode nommée RemoveUsageRights() a été ajoutée à la classe PdfFileSignature. Une autre méthode nommée ContainsUsageRights() est ajoutée pour déterminer si le PDF source contient des droits étendus.

{{% alert color="primary" %}}
À partir d'Aspose.PDF pour .NET 9.5.0, les noms des méthodes suivantes sont mis à jour. Veuillez noter que les méthodes précédentes sont toujours dans l'API mais elles ont été marquées comme obsolètes et seront supprimées. Par conséquent, il est recommandé d'essayer d'utiliser les méthodes mises à jour.

- La méthode IsContainSignature(.) a été renommée ContainsSignature(..).

- La méthode IsCoversWholeDocument(..) a été renommée CoversWholeDocument(..).{{% /alert %}}

Le code suivant montre comment supprimer les droits d'utilisation du document :

```csharp
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
string input = dataDir + "DigitallySign.pdf";
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(input);
    if (pdfSign.ContainsUsageRights())
    {
        pdfSign.RemoveUsageRights();
    }

    pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
}
```