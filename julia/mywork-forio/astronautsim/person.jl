#julia

type Person
    name::String
end

typealias Mom Person
typealias Boss Person
typealias Doctor Person

function call_person(person)
    print("Hello $person.name")
end

function call_person(person::Mom)
    print("I love you, mom")
end

function call_person(person::Boss):
    print("Sorry I'm late $person.name")
end

function call_person(person::Doctor)
    print("what's up, doc?\n")
end

doc = Doctor("Rich")

call_person(doc)
