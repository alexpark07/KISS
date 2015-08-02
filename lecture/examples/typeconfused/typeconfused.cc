// Fedora 20 x64: gcc ./confused.cc -lstdc++
#include <unistd.h>
 
class IShouldRunCalculator { public: virtual bool UWannaRun() = 0; };
 
class CalculatorDecider final : public IShouldRunCalculator {
public:
    CalculatorDecider() : m_run(false) {}
    virtual bool UWannaRun() { return m_run; }
private: bool m_run;
};
 
class DelegatingCalculatorDecider final : public IShouldRunCalculator {
public:
    DelegatingCalculatorDecider(IShouldRunCalculator* delegate) : m_delegate(delegate) {}
    virtual bool UWannaRun() { return m_delegate->UWannaRun(); }
private: IShouldRunCalculator* m_delegate;
};
 
int main() {
    CalculatorDecider nonono;
    DelegatingCalculatorDecider isaidno(&nonono);
    IShouldRunCalculator* decider = &isaidno;
    CalculatorDecider* confused_decider = reinterpret_cast<CalculatorDecider*>(decider);
    if (confused_decider->UWannaRun()) execl("/usr/bin/gnome-calculator", 0);
}
