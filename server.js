import express from 'express';

const app = express();
app.use(express.json())

const user = [];

// Corrigido a ordem dos parâmetros: (req, res)
app.post('/usuarios', (req, res) => {
    user.push(req.body); // Se estiver enviando um corpo com JSON, use req.body
    res.status(201).json(req.body);
});

app.get('/usuarios', (req, res) => {
    res.status(200).json(user)
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});



// tipo de rota / metodo htpp ( get(gerar lista), post (criar), put(editar varios), patch(editar um), delete(deletar)) + endereço

/*obj - criar api de usuários
    - Criar um usuário
    - listar Todos os Usuários
    - Editar um usuario
    - Deletar um usuário
*/

// ordem importa - req, res
