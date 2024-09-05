import express from 'express';

const app = express();

const user = [];

// Corrigido a ordem dos parâmetros: (req, res)
app.post('/usuarios', (req, res) => {
    console.log(req.body); // Se estiver enviando um corpo com JSON, use req.body
    res.send('Ok, deu certo');
});

app.get('/usuarios', (req, res) => {
    res.send('OK, deu bom');
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
