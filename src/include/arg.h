#ifndef __ARG_H
#define __ARG_H

#include <ostream>
#include <variant>
#include <string>
#include "types.h"

struct Arg {
    enum Type { NUM, STR, IDENT };

    Type type;
    std::variant<std::string, f32> data;

    Arg();

    Arg(const std::string& str, Type type);

    Arg(f32 val);

    Arg(const char* str);

    ~Arg() = default;

    f32 get_num() const;
    std::string get_str() const ;

    const char* type_to_cstr() const;
};

std::ostream& operator<<(std::ostream& os, const Arg& a);

#endif  //__ARG_H
