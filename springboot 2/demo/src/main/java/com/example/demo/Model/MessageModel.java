import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "tasks")
public class MessageModel {

    @Id
    private String id;
    private String text;

    public Task() {}

    public Task(String text) {
        this.text = text;
    }

    public String getId() { return id; }

    public String getText() { return text; }

    public void setText(String text) {
        this.text = text;
    }
}