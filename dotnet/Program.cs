using MySql.Data.MySqlClient;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => new { Message = "Hello World" });

app.MapGet("/users", () =>
{
    var users = new List<User>();
    using (var connection = new MySqlConnection("Server=localhost;Database=test;Uid=test-user;Pwd=test-user-password;"))
    {
        connection.Open();
        var query = "SELECT * FROM users";
        using (var command = new MySqlCommand(query, connection))
        {
            using (var reader = command.ExecuteReader())
            {
                while (reader.Read())
                {
                    var user = new User
                    {
                        Id = reader.GetInt32(0),
                        Name = reader.GetString(1),
                        Email = reader.GetString(2)
                    };
                    users.Add(user);
                }
            }
        }
    }

    return users;
});

app.Run();

public class User
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public string Email { get; set; } = string.Empty;
}
