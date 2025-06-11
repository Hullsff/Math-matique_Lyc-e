# Je vous partage ici ma réfléxion par rapport au projet Polynôme : 

### 1. Idée de base : 
Je veux générer un polynôme de degré 3, 4 ou 5. 
Il faut que je donne son expression développée
Et donc pour Python, ses coefficients. 

### 2. Manière de faire : 
Je vais construire un polynôme P en produit de facteur de polynome AUTRE de degré 1 ou 2. 
Vous l'aurez compris, au lieu de crée des polynomes P et de vérifier les racines évidentes, je construis un polynômes directement de la forme : 
Par exemple : P(x) = (x+3)(x+1)(x^2 + 2x-5) 

### 3. Traduction en langage Python : 
- Chaque polynôme est représenté par une liste de coefficient 
Par exemple : P(x) = 2 + 3x + x^2 = [2;3;1]
Plus formellement, j'écris les polynômes P en base (1;X;X^2) 

### 4. Multiplication de polynômes :
Pour multiplier les polynômes entre eux, j'ai crée une fonction spécifique PRODUIT

### 5. Cas par cas selon le degré 
- Degré 3 : degré 1 * trinome du second degré 
- degré 4 : degré 1 * degré 1 * trinome du second degré 
- degré 5 : degré 1 * degré 1 * degré 1 * trinome du second degré 

### 6. Affichage : 
Affichage simple et classique. 
