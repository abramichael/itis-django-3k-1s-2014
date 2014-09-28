@interface A {

}

public class MyClass {
	
	@A
	public static void f() {
	
	}
	
	public static void main(String [] args) {
		f();
	}
}