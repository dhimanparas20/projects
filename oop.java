class Person {
    String name;
    public Person(String name) {
        this.name = name;
    }
    String getName(){
        String data = this.name;
        return data;
    }
}


public class Oop {
    public static void print(String data){
        System.out.println(data);
    }
    public static void main(String[] args){
        //System.out.println("hello World");
        Person p1 = new Person("Aman");
        String name = p1.getName();
        print("Your name is: "+name);
    }    
}




