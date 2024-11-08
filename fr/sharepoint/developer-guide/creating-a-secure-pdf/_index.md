---

title: Créer un PDF Sécurisé dans SharePoint

linktitle: Création d'un PDF Sécurisé

type: docs

weight: 60

url: /fr/sharepoint/creating-a-secure-pdf/

lastmod: "2020-12-16"

description: En utilisant l'API PDF SharePoint, vous pouvez produire des PDF sécurisés, cryptés et spécifier leurs mots de passe dans SharePoint.

---



{{% alert color="primary" %}}



Aspose.PDF pour SharePoint prend en charge la création de PDF sécurisés. L'installation d'Aspose.PDF pour SharePoint ajoute une option **Paramètres de Sécurité PDF** dans les Paramètres du Site. Ici, vous pouvez définir le mot de passe utilisateur, le mot de passe propriétaire et toute valeur de la liste des algorithmes pour crypter le PDF de sortie. La liste des algorithmes offre différentes combinaisons d'algorithmes de cryptage et de tailles de clés. Passez la valeur de votre choix.



Cet article démontre comment utiliser Aspose.PDF pour SharePoint pour générer un PDF crypté.



{{% /alert %}}



## **Création d'un PDF Sécurisé**



Pour démontrer la fonctionnalité, nous configurons d'abord l'option **Paramètres de Sécurité PDF** pour le mot de passe propriétaire et utilisateur et l'algorithme de cryptage. L'exemple fusionne ensuite deux documents d'une bibliothèque de documents.



### **Définir les options de paramétrage sécurisé PDF**



Ouvrez l'option **Paramètres sécurisés PDF** depuis les paramètres du site et définissez l'algorithme, le mot de passe propriétaire et le mot de passe utilisateur.



Spécifiez différents mots de passe utilisateur et propriétaire lors du cryptage du fichier PDF.



- Le mot de passe utilisateur, s'il est défini, est ce que vous devez fournir pour ouvrir un PDF. Acrobat Reader demande à l'utilisateur de saisir le mot de passe utilisateur. S'il est incorrect, le document ne s'ouvre pas.

- Le mot de passe propriétaire, s'il est défini, contrôle les autorisations telles que l'impression, l'édition, l'extraction, les commentaires, etc. Acrobat Reader interdit ces fonctionnalités en fonction des paramètres d'autorisation. Acrobat nécessite ce mot de passe si vous souhaitez définir/modifier les autorisations.



![todo:image_alt_text](creating-a-secure-pdf_1.png)



### **Fusionner des documents**



Fusionnez deux documents en utilisant l'option **Convertir en PDF**. Cette fonctionnalité fusionne plusieurs fichiers non-PDF (HTML, texte ou image) en un fichier PDF.



1. Ouvrez une bibliothèque de documents et sélectionnez les documents souhaités dans la liste.

![todo:image_alt_text](creating-a-secure-pdf_2.png)

1. Utilisez l'option **Fusionner en PDF** des Outils de bibliothèque pour enregistrer le fichier de sortie. Il vous est demandé d'enregistrer le fichier de sortie sur le disque.

![todo:image_alt_text](creating-a-secure-pdf_3.png)

### **Sortie**

Le fichier de sortie est crypté.

![todo:image_alt_text](creating-a-secure-pdf_4.png)