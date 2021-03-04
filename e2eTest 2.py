


    def test_apply_raise(self):
        print("test_apply_raise")
        emp_1 = Employee("Nilly", "willy", 85200)
        emp_2 = Employee("Rilly", "rally", 56000)


        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay,88608 )
        self.assertEqual(emp_2.pay,58240 )



    def test_email(self):
        print("test_email")
        emp_1 = Employee("Nilly", "willy", 85200)
        emp_2 = Employee("Rilly", "rally", 56000)

        self.assertEqual(emp_1.email, "Nilly.willy@email.com")
        self.assertEqual(emp_2.email, "Rilly.rally@email.com")

        emp_1.first = "Jamanzi"
        emp_2.first = "Pithaji"

        self.assertEqual(emp_1.email, "Jamanzi.willy@email.com")
        self.assertEqual(emp_2.email, "Pithaji.rally@email.com")

if __name__ =="__main__":
    unittest.main()
"""
    print(emp_1.pay)
    print(emp_3.fullname)
    print(emp_1.fullname)
    print(emp_1.email)
    print(emp_1.pay)
    emp_1.apply_raise()
    print(emp_1.pay)
    emp_2.apply_raise()
    print(emp_2.pay)
		


